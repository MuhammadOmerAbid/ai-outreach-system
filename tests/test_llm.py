import pytest


def test_ask_returns_string(monkeypatch):
    import shared.llm as llm_mod

    class FakeContent:
        text = "mocked response"

    class FakeMsg:
        content = [FakeContent()]

    class FakeMessages:
        def create(self, **kwargs):
            return FakeMsg()

    class FakeClient:
        messages = FakeMessages()

    monkeypatch.setattr(llm_mod, "_client", FakeClient())
    result = llm_mod.ask(system="sys", user="hi")
    assert result == "mocked response"
