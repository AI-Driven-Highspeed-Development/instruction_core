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
    
    Supports two sync modes via config (both accept lists of target directories):
    - official_target_dir: List of paths. Syncs from cores/instruction_core/data to each target
    - custom_target_dir: List of paths. Syncs from ./project/data/instruction_core (or config path) to each target
    
    Empty lists or empty strings within lists are skipped.
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
        custom_data_path = self.config.path.data
        self.custom_source_path = (self.root_path / custom_data_path).resolve()
        
        # Target directories from config (now lists)
        official_targets = self.config.path.official_target_dir
        custom_targets = self.config.path.custom_target_dir
        
        # Convert to lists of resolved paths, filtering out empty strings
        self.official_target_paths = [
            (self.root_path / target).resolve() 
            for target in (official_targets if isinstance(official_targets, list) else [official_targets])
            if target
        ]
        self.custom_target_paths = [
            (self.root_path / target).resolve()
            for target in (custom_targets if isinstance(custom_targets, list) else [custom_targets])
            if target
        ]

    def _ensure_target_structure(self, target_path: Path) -> None:
        """Ensure instructions, agents, and prompts directories exist under target path."""
        try:
            (target_path / "instructions").mkdir(parents=True, exist_ok=True)
            (target_path / "agents").mkdir(parents=True, exist_ok=True)
            (target_path / "prompts").mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Ensured target structure exists at {target_path}")
        except OSError as e:
            raise ADHDError(f"Failed to create target structure at {target_path}: {e}") from e

    def _sync_files_by_pattern(self, source_dir: Path, target_dir: Path, pattern: str, subdir: str, label: str) -> None:
        """
        Sync files matching a pattern from source subdirectory to target subdirectory.
        
        Args:
            source_dir: Source directory containing the subdir
            target_dir: Target directory containing the subdir
            pattern: Glob pattern for files (e.g., "*.instructions.md")
            subdir: Subdirectory name (e.g., "instructions", "agents", "prompts")
            label: Label for logging
        """
        src = source_dir / subdir
        if src.exists():
            for file_path in src.glob(pattern):
                try:
                    dest_path = target_dir / subdir / file_path.name
                    shutil.copy2(file_path, dest_path)
                    self.logger.info(f"Synced {subdir[:-1]} ({label}): {file_path.name}")
                except OSError as e:
                    self.logger.error(f"Failed to sync {file_path.name} to {subdir}: {e}")

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

        self._sync_files_by_pattern(source_path, target_path, "*.instructions.md", "instructions", label)
        self._sync_files_by_pattern(source_path, target_path, "*.agent.md", "agents", label)
        self._sync_files_by_pattern(source_path, target_path, "*.prompt.md", "prompts", label)

    def _sync_module_files_to_target(self, target_path: Path, pattern: str, subdir: str, file_type: str) -> None:
        """
        Scan all modules and copy files matching pattern to target subdirectory.
        
        Args:
            target_path: Target base directory
            pattern: Glob pattern (e.g., "*.instructions.md")
            subdir: Target subdirectory (e.g., "instructions")
            file_type: Human-readable file type for logging (e.g., "instruction")
        """
        self.logger.info(f"Syncing module {file_type}s to {target_path}...")
        
        report = self.modules_controller.list_all_modules()
        
        for module in report.modules:
            files = list(module.path.glob(pattern))
            if files:
                for file_path in files:
                    try:
                        dest_path = target_path / subdir / file_path.name
                        shutil.copy2(file_path, dest_path)
                        self.logger.info(f"Synced module {file_type}: {module.name} -> {dest_path.name}")
                    except OSError as e:
                        self.logger.error(f"Failed to sync {file_type} {file_path.name} for module {module.name}: {e}")
            else:
                self.logger.debug(f"No {file_type}s found for module {module.name}")

    def run(self) -> None:
        """Execute the full synchronization process based on config."""
        self.logger.info("Starting instruction synchronization...")
        
        # Sync official source to all official targets
        if self.official_target_paths:
            for target_path in self.official_target_paths:
                self.logger.info(f"Official sync: {self.official_source_path} -> {target_path}")
                self._ensure_target_structure(target_path)
                self._sync_data_to_target(self.official_source_path, target_path, "official")
                self._sync_module_files_to_target(target_path, "*.instructions.md", "instructions", "instruction")
                self._sync_module_files_to_target(target_path, "*.agent.md", "agents", "agent")
                self._sync_module_files_to_target(target_path, "*.prompt.md", "prompts", "prompt")
        else:
            self.logger.info("No official targets configured, skipping official sync.")
        
        # Sync custom source to all custom targets
        if self.custom_target_paths:
            for target_path in self.custom_target_paths:
                self.logger.info(f"Custom sync: {self.custom_source_path} -> {target_path}")
                self._ensure_target_structure(target_path)
                self._sync_data_to_target(self.custom_source_path, target_path, "custom")
        else:
            self.logger.info("No custom targets configured, skipping custom sync.")
        
        self.logger.info("Instruction synchronization completed.")
