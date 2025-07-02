from tradingagents.graph.trading_graph import TradingAgentsGraph

class DummyGraph:
    def __init__(self, state):
        self.state = state
    def invoke(self, init_state, **kwargs):
        return self.state

class DummyPropagator:
    def create_initial_state(self, company_name, trade_date):
        return {}
    def get_graph_args(self):
        return {}

class DummySignalProcessor:
    def __init__(self, result):
        self.result = result
    def process_signal(self, full_signal):
        return self.result

def test_propagate():
    dummy_state = {"final_trade_decision": "dummy"}
    tg = TradingAgentsGraph.__new__(TradingAgentsGraph)
    tg.graph = DummyGraph(dummy_state)
    tg.propagator = DummyPropagator()
    tg.signal_processor = DummySignalProcessor("BUY")
    tg._log_state = lambda trade_date, state: None
    tg.debug = False
    tg.curr_state = None
    tg.log_states_dict = {}
    result_state, decision = TradingAgentsGraph.propagate(tg, "AAPL", "2024-01-01")
    assert result_state == dummy_state
    assert decision == "BUY"
