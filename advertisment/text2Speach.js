import fs from "fs";
import path from "path";
import OpenAI from "openai";
import { randomUUID } from "crypto";

const openai = new OpenAI({apiKey:'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'});

const speechFile = path.resolve("./output/" + randomUUID() + ".mp3");
const input = "testing 123, testing here, can anyone hear me?"

async function main() {
  const mp3 = await openai.audio.speech.create({
    model: "tts-1",
    voice: "alloy",
    input: input,
  });
  console.log(speechFile);
  const buffer = Buffer.from(await mp3.arrayBuffer());
  await fs.promises.writeFile(speechFile, buffer);
}
main();