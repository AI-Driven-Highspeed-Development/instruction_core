from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

from cores.exceptions_core.adhd_exceptions import ADHDError
from cores.modules_controller_core.modules_controller import ModulesController
from managers.config_manager import ConfigManager
from utils.logger_util.logger import Logger


class InstructionController:
    """
    Controller for managing instruction and agent files.
    
    Supports two sync modes via config:
    - official_target_dir: Syncs from cores/instruction_core/data to specified target
    - custom_target_dir: Syncs from ./project/data/instruction_core (or config path) to specified target
    
    If a target dir is empty string, that sync is skipped.
    """

    def __init__(self, root_path: Optional[Path] = None, logger: Optional[Logger] = None):
        self.root_path = (root_path or Path.cwd()).resolve()
        self.logger = logger or Logger(name=__class__.__name__)
        self.modules_controller = ModulesController(root_path=self.root_path)
        
        # Load config
        cm = ConfigManager()
        self.config = cm.config.instruction_core
        
        # Official source: cores/instruction_core/data
        self.official_source_path = self.root_path / "cores" / "instruction_core" / "data"
        
        # Custom source: from config path.data or default
        custom_data_path = self.config.path.data if hasattr(self.config.path, 'data') else "./project/data/instruction_core"
        self.custom_source_path = (self.root_path / custom_data_path).resolve()
        
        # Target directories from config
        official_target = getattr(self.config.path, 'official_target_dir', './.github')
        custom_target = getattr(self.config.path, 'custom_target_dir', '')
        
        self.official_target_path = (self.root_path / official_target).resolve() if official_target else None
        self.custom_target_path = (self.root_path / custom_target).resolve() if custom_target else None

    def _ensure_target_structure(self, target_path: Path) -> None:
        """Ensure instructions, agents, and prompts directories exist under target path."""
        try:
            (target_path / "instructions").mkdir(parents=True, exist_ok=True)
            (target_path / "agents").mkdir(parents=True, exist_ok=True)
            (target_path / "prompts").mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Ensured target structure exists at {target_path}")
        except OSError as e:
            raise ADHDError(f"Failed to create target structure at {target_path}: {e}") from e

    def _sync_data_to_target(self, source_path: Path, target_path: Path, label: str) -> None:
        """
        Sync instruction, agent, and prompt files from source to target.
        
        Args:
            source_path: Source directory containing instructions/, agents/, prompts/ subdirs
            target_path: Target directory (e.g., .github)
            label: Label for logging (e.g., "official", "custom")
        """
        if not source_path.exists():
            self.logger.info(f"{label} source path not found: {source_path}. Skipping.")
            return

        self.logger.info(f"Syncing {label} data from {source_path} to {target_path}")

        try:
            # Sync instructions
            instructions_src = source_path / "instructions"
            if instructions_src.exists():
                for file_path in instructions_src.glob("*.instructions.md"):
                    dest_path = target_path / "instructions" / file_path.name
                    shutil.copy2(file_path, dest_path)
                    self.logger.info(f"Synced instruction ({label}): {file_path.name}")

            # Sync agents
            agents_src = source_path / "agents"
            if agents_src.exists():
                for file_path in agents_src.glob("*.agent.md"):
                    dest_path = target_path / "agents" / file_path.name
                    shutil.copy2(file_path, dest_path)
                    self.logger.info(f"Synced agent ({label}): {file_path.name}")

            # Sync prompts
            prompts_src = source_path / "prompts"
            if prompts_src.exists():
                for file_path in prompts_src.glob("*.prompt.md"):
                    dest_path = target_path / "prompts" / file_path.name
                    shutil.copy2(file_path, dest_path)
                    self.logger.info(f"Synced prompt ({label}): {file_path.name}")

        except OSError as e:
            raise ADHDError(f"Failed to sync {label} data: {e}") from e

    def _sync_module_instructions_to_target(self, target_path: Path) -> None:
        """
        Scan all modules and copy <module_name>.instructions.md to target/instructions.
        """
        self.logger.info(f"Syncing module instructions to {target_path}...")
        
        report = self.modules_controller.list_all_modules()
        
        for module in report.modules:
            candidates = [
                module.path / f"{module.name}.instructions.md",
                module.module_type.path / f"{module.name}.instructions.md"
            ]
            
            source_path: Optional[Path] = None
            for candidate in candidates:
                if candidate.exists():
                    source_path = candidate
                    break
            
            if source_path:
                try:
                    dest_path = target_path / "instructions" / source_path.name
                    shutil.copy2(source_path, dest_path)
                    self.logger.info(f"Synced module instruction: {module.name} -> {dest_path.name}")
                except OSError as e:
                    self.logger.error(f"Failed to sync instruction for module {module.name}: {e}")
            else:
                self.logger.debug(f"No instructions found for module {module.name}")

    def _sync_module_agents_to_target(self, target_path: Path) -> None:
        """
        Scan all modules and copy *.agent.md files to target/agents.
        """
        self.logger.info(f"Syncing module agents to {target_path}...")
        
        report = self.modules_controller.list_all_modules()
        
        for module in report.modules:
            for agent_file in module.path.glob("*.agent.md"):
                try:
                    dest_path = target_path / "agents" / agent_file.name
                    shutil.copy2(agent_file, dest_path)
                    self.logger.info(f"Synced module agent: {module.name} -> {dest_path.name}")
                except OSError as e:
                    self.logger.error(f"Failed to sync agent {agent_file.name} for module {module.name}: {e}")

    def run(self) -> None:
        """Execute the full synchronization process based on config."""
        self.logger.info("Starting instruction synchronization...")
        
        # Sync official source to official target (if configured)
        if self.official_target_path:
            self.logger.info(f"Official sync: {self.official_source_path} -> {self.official_target_path}")
            self._ensure_target_structure(self.official_target_path)
            self._sync_data_to_target(self.official_source_path, self.official_target_path, "official")
            self._sync_module_instructions_to_target(self.official_target_path)
            self._sync_module_agents_to_target(self.official_target_path)
        else:
            self.logger.info("Official target not configured, skipping official sync.")
        
        # Sync custom source to custom target (if configured)
        if self.custom_target_path:
            self.logger.info(f"Custom sync: {self.custom_source_path} -> {self.custom_target_path}")
            self._ensure_target_structure(self.custom_target_path)
            self._sync_data_to_target(self.custom_source_path, self.custom_target_path, "custom")
        else:
            self.logger.info("Custom target not configured, skipping custom sync.")
        
        self.logger.info("Instruction synchronization completed.")
