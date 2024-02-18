const OpenAI = require("openai")

const openai = new OpenAI({apiKey: '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'});
const userInput = "what is the best color for food in the world?"
async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{"role": "system", "content": "You are a helpful assistant."}, {"role":"user", "content":userInput}],
    model: "gpt-3.5-turbo"
  });

  console.log(completion.choices[0]);
}
main();