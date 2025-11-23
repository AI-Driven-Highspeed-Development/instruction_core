from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

from cores.exceptions_core.adhd_exceptions import ADHDError
from cores.modules_controller_core.modules_controller import ModulesController
from utils.logger_util.logger import Logger


class InstructionController:
    """
    Controller for managing instruction and agent files.
    Syncs files from cores/instruction_core/data and individual modules to .github/.
    """

    def __init__(self, root_path: Optional[Path] = None, logger: Optional[Logger] = None):
        self.root_path = (root_path or Path.cwd()).resolve()
        self.logger = logger or Logger(name=__class__.__name__)
        self.modules_controller = ModulesController(root_path=self.root_path)
        
        # Define paths
        self.core_data_path = self.root_path / "cores" / "instruction_core" / "data"
        self.core_instructions_path = self.core_data_path / "instructions"
        self.core_agents_path = self.core_data_path / "agents"
        self.core_prompts_path = self.core_data_path / "prompts"
        self.github_instructions_path = self.root_path / ".github" / "instructions"
        self.github_agents_path = self.root_path / ".github" / "agents"
        self.github_prompts_path = self.root_path / ".github" / "prompts"
        self.github_adhd_agents_path = self.github_agents_path

    def ensure_github_structure(self) -> None:
        """Ensure .github/instructions, .github/agents and .github/prompts directories exist."""
        try:
            self.github_instructions_path.mkdir(parents=True, exist_ok=True)
            self.github_agents_path.mkdir(parents=True, exist_ok=True)
            self.github_prompts_path.mkdir(parents=True, exist_ok=True)
            self.github_adhd_agents_path.mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Ensured .github structure exists at {self.root_path / '.github'}")
        except OSError as e:
            raise ADHDError(f"Failed to create .github structure: {e}") from e

    def sync_core_data(self) -> None:
        """
        Copy .instructions.md, .agent.md and *.prompt.md files from cores/instruction_core/data
        into .github/instructions, .github/agents and .github/prompts respectively.
        Overwrites existing files.
        """
        if not self.core_data_path.exists():
            self.logger.info(f"Core data path not found: {self.core_data_path}. Skipping core data sync.")
            return

        self.logger.info(f"Syncing core data from {self.core_data_path}")

        try:
            # Sync instructions
            if self.core_instructions_path.exists():
                for file_path in self.core_instructions_path.glob("*.instructions.md"):
                    dest_path = self.github_instructions_path / file_path.name
                    shutil.copy2(file_path, dest_path)
                    self.logger.info(f"Synced instruction: {file_path.name}")
            else:
                self.logger.debug(f"Core instructions path not found: {self.core_instructions_path}")

            # Sync agents
            if self.core_agents_path.exists():
                for file_path in self.core_agents_path.glob("*.agent.md"):
                    if ".adhd.agent.md" in file_path.name:
                        dest_path = self.github_adhd_agents_path / file_path.name
                    else:
                        dest_path = self.github_agents_path / file_path.name
                    shutil.copy2(file_path, dest_path)
                    self.logger.info(f"Synced agent: {file_path.name}")
            else:
                self.logger.debug(f"Core agents path not found: {self.core_agents_path}")

            # Sync prompts
            if self.core_prompts_path.exists():
                for file_path in self.core_prompts_path.glob("*.prompt.md"):
                    dest_path = self.github_prompts_path / file_path.name
                    shutil.copy2(file_path, dest_path)
                    self.logger.info(f"Synced prompt: {file_path.name}")
            else:
                self.logger.debug(f"Core prompts path not found: {self.core_prompts_path}")

        except OSError as e:
            raise ADHDError(f"Failed to sync core data: {e}") from e

    def sync_module_instructions(self) -> None:
        """
        Scan all modules and copy <module_name>.instructions.md to .github/instructions.
        Overwrites existing files.
        """
        self.logger.info("Syncing module instructions...")
        
        report = self.modules_controller.list_all_modules()
        
        for module in report.modules:
            # Potential locations
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
                    dest_path = self.github_instructions_path / source_path.name
                    shutil.copy2(source_path, dest_path)
                    self.logger.info(f"Synced module instruction: {module.name} -> {dest_path.name}")
                except OSError as e:
                    # Log error but continue syncing other modules
                    self.logger.error(f"Failed to sync instruction for module {module.name}: {e}")
            else:
                # It's okay if a module doesn't have instructions, just debug log
                self.logger.debug(f"No instructions found for module {module.name}")

    def run(self) -> None:
        """Execute the full synchronization process."""
        self.logger.info("Starting instruction synchronization...")
        self.ensure_github_structure()
        self.sync_core_data()
        self.sync_module_instructions()
        self.logger.info("Instruction synchronization completed.")
