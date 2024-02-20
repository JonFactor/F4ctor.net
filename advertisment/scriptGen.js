const OpenAI = require("openai")

const openai = new OpenAI({apiKey: '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'});
const userInput = "what is the best color for food in the world?"
const userStats = [6,4,3,6,3]
const prompt = `Create a script for a one minute advertisemnt off of the following user input: ${userInput}, and with the following stats for the add:
sob-story: ${userStats[0]}, family-oriented: ${userStats[1]}, meta: ${userStats[2]}, good-feeling: ${userStats[3]}, community around product: ${userStats[4]}
`
async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{"role": "system", "content": "You are a helpful assistant."}, {"role":"user", "content":prompt}],
    model: "gpt-3.5-turbo"
  });

  console.log(completion.choices[0]);
}
main();