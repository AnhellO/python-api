import pytest

from coalesce import AverageCoalesceConcreteStrategy, MaxCoalesceConcreteStrategy, MinCoalesceConcreteStrategy, CoalesceContext

@pytest.mark.parametrize("responses, expected", [
    (
        (
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 5000
            },
            {
                "deductible": 1200,
                "stop_loss": 13000,
                "oop_max": 6000
            },
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 6000
            }
        ),
        {
            "deductible": 1066,
            "stop_loss": 11000,
            "oop_max": 5666
        }
    )
])
def test_default(responses, expected):
    context = CoalesceContext(responses)
    assert context.execute_strategy() == expected

@pytest.mark.parametrize("concrete_strategy, responses, expected", [
    (
        MaxCoalesceConcreteStrategy(),
        (
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 5000
            },
            {
                "deductible": 1200,
                "stop_loss": 13000,
                "oop_max": 6000
            },
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 6000
            }
        ),
        {
            "deductible": 1200,
            "stop_loss": 13000,
            "oop_max": 6000
        }
    ),
    (
        MinCoalesceConcreteStrategy(),
        (
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 5000
            },
            {
                "deductible": 1200,
                "stop_loss": 13000,
                "oop_max": 6000
            },
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 6000
            }
        ),
        {
            "deductible": 1000,
            "stop_loss": 10000,
            "oop_max": 5000
        }
    )
])
def test_specifics(concrete_strategy, responses, expected):
    context = CoalesceContext(responses, concrete_strategy)
    assert context.execute_strategy() == expected
    
@pytest.mark.parametrize("concrete_strategy_1, concrete_strategy_2, expected_1, expected_2, responses", [
    (
        MaxCoalesceConcreteStrategy(),
        AverageCoalesceConcreteStrategy(),
        {
            "deductible": 1200,
            "stop_loss": 13000,
            "oop_max": 6000
        },
        {
            "deductible": 1066,
            "stop_loss": 11000,
            "oop_max": 5666
        },
        (
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 5000
            },
            {
                "deductible": 1200,
                "stop_loss": 13000,
                "oop_max": 6000
            },
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 6000
            }
        )
    )
])
def test_configuring_strategy(concrete_strategy_1, concrete_strategy_2, expected_1, expected_2, responses):
    context = CoalesceContext(responses, concrete_strategy_1)
    assert context.execute_strategy() == expected_1
    
    context.set_strategy(concrete_strategy_2)
    assert context.execute_strategy() == expected_2