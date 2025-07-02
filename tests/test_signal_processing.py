import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "signal_processing", Path("tradingagents/graph/signal_processing.py")
)
signal_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(signal_module)
SignalProcessor = signal_module.SignalProcessor

class DummyLLM:
    def __init__(self, response):
        self.response = response
    def invoke(self, messages):
        class R:
            def __init__(self, content):
                self.content = content
        return R(self.response)

def test_process_signal():
    sp = SignalProcessor(DummyLLM("BUY"))
    assert sp.process_signal("any") == "BUY"
