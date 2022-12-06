import gc
from prompt_toolkit.shortcuts.prompt import PromptSession


def _count_prompt_session_instances() -> int:
    # Run full GC collection first.
    gc.collect()

    # Count number of remaining referenced `PromptSession` instances.
    objects = gc.get_objects()
    return len([obj for obj in objects if isinstance(obj, PromptSession)])


def test_prompt_session_memory_leak() -> None:
    before_count = _count_prompt_session_instances()
    assert before_count == 0

    p = PromptSession()

    after_count = _count_prompt_session_instances()
    assert after_count == before_count + 1

    del p

    after_delete_count = _count_prompt_session_instances()
    assert after_delete_count == before_count
