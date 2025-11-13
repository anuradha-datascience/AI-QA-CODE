import json, pytest

@pytest.mark.parametrize("prompt", json.load(open("data/prompts.json"))["prompts"])
def test_gemini_prompt(gemini_client, logger, prompt):
    response = gemini_client.generate_content(prompt)
    logger.info(f"Prompt: {prompt}")
    logger.info(f"Response: {response.text[:200]}")
    assert response.text, "Gemini returned empty response!"
    assert isinstance(response.text, str)
