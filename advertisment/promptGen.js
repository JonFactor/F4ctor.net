const OpenAI = require("openai")

const inputFromUser = ["ages 12-18", "is a toy shop opening soon", "330-519-9231", "25% off first time users", "the best deals in the vally"]
const inputStats = [6,4,7,2,4,7,9,4,10, 1]
const openai = new OpenAI({apiKey: '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'});
const userInput = `Create a prompt for a video ai model that describles an add with these charisorics out of a scale of 1-10, 
10 being the best and 1 being the worst. Take into account that this add is targeted twoards: ${inputFromUser[0]}. this add is for a company that: ${inputFromUser[1]}
. the phone number for said company is ${inputFromUser[2]}, and they are having a deal that needs to be mentioned of: ${inputFromUser[3]}. They also would like the phrase
: ${inputFromUser[4]} to be inclueded as well. Along with the following stats being added to the production of the prompt for the video: ${inputStats[0]} = family orented,
${inputStats[1]} = heartfelt, ${inputStats[2]} = heartstrings, ${inputStats[3]} = community-feeling, ${inputStats[4]} = larger-than-life felling, ${inputStats[5]} = fighting-for-the-people feeling
${inputStats[6]} = important-beyond-belife, ${inputStats[7]} = a-tack-video-add, ${inputStats[8]} = relating-to-the-customer feeling. The video must fit into a 1 min window`
async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{"role": "system", "content": "You are a helpful assistant."}, {"role":"user", "content":userInput}],
    model: "gpt-3.5-turbo"
  });

  console.log(completion.choices[0]);
}
main();