"""
MemMimic - The Memory System That Learns You Back

A contextual memory intelligence system for AI.
"""

__version__ = "1.0.0"
__author__ = "Sprooket & Claude"

# Main API
from .api import MemMimicAPI, create_memmimic

# Core components (for advanced users)
from .memory import UnifiedMemoryStore, MemoryStore, Memory, ContextualAssistant
from .tales import TaleManager
from .cxd import (
    CXDFunction,
    ExecutionState,
    CXDTag, 
    CXDSequence,
    OptimizedMetaCXDClassifier,
    create_optimized_classifier,
)

__all__ = [
    # Main API (most users)
    "MemMimicAPI",
    "create_memmimic",
    
    # Core components (advanced users)
    "UnifiedMemoryStore",
    "MemoryStore", 
    "Memory",
    "ContextualAssistant",
    "TaleManager",
    
    # CXD Framework
    "CXDFunction",
    "ExecutionState",
    "CXDTag",
    "CXDSequence", 
    "OptimizedMetaCXDClassifier",
    "create_optimized_classifier",
]
