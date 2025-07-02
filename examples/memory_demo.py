from tradingagents.agents.utils.memory import FinancialSituationMemory

if __name__ == "__main__":
    matcher = FinancialSituationMemory("demo", {
        "backend_url": "https://api.openai.com/v1"
    })

    example_data = [
        (
            "High inflation rate with rising interest rates and declining consumer spending",
            "Consider defensive sectors like consumer staples and utilities. Review fixed-income portfolio duration.",
        ),
        (
            "Tech sector showing high volatility with increasing institutional selling pressure",
            "Reduce exposure to high-growth tech stocks. Look for value opportunities in established tech companies with strong cash flows.",
        ),
        (
            "Strong dollar affecting emerging markets with increasing forex volatility",
            "Hedge currency exposure in international positions. Consider reducing allocation to emerging market debt.",
        ),
        (
            "Market showing signs of sector rotation with rising yields",
            "Rebalance portfolio to maintain target allocations. Consider increasing exposure to sectors benefiting from higher rates.",
        ),
    ]

    matcher.add_situations(example_data)

    current_situation = """
    Market showing increased volatility in tech sector, with institutional investors
    reducing positions and rising interest rates affecting growth stock valuations
    """

    recommendations = matcher.get_memories(current_situation, n_matches=2)

    for i, rec in enumerate(recommendations, 1):
        print(f"\nMatch {i}:")
        print(f"Similarity Score: {rec['similarity_score']:.2f}")
        print(f"Matched Situation: {rec['matched_situation']}")
        print(f"Recommendation: {rec['recommendation']}")
