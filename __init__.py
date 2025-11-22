import os
import sys
from pathlib import Path

# Add path handling to work from the new nested directory structure
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.getcwd()  # Use current working directory as project root
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from cores.instruction_core.instruction_controller import InstructionController
from utils.logger_util.logger import Logger

__all__ = ["InstructionController"]

if __name__ == "__main__":
    # This block is executed when the file is run as a script,
    # e.g. by ProjectInit during project initialization.
    logger = Logger(name="InstructionCoreInit")
    logger.info("Running instruction core initialization...")
    try:
        controller = InstructionController(root_path=Path.cwd(), logger=logger)
        controller.run()
        logger.info("Instruction core initialization completed.")
    except Exception as e:
        logger.error(f"Instruction core initialization failed: {e}")
        sys.exit(1)