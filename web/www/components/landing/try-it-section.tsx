"use client";

import { useState } from "react";

const tabs = ["Translation", "Tone Marking", "Proverbs"];

const codeExamples: Record<string, { command: string; output: string }> = {
  Translation: {
    command: `curl -X POST https://api.yoruba-api.dev/v1/translate \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{"word": "Hello", "lang": "yo", "use_ai": true}'`,
    output: `{
  "original": "Hello",
  "translated": "Pẹ̀lẹ́ o / Ẹ kúùbọ̀",
  "source": "ai",
  "confidence": 0.98
}`,
  },
  "Tone Marking": {
    command: `curl -X POST https://api.yoruba-api.dev/v1/tone-mark \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{"text": "Omo Oduduwa"}'`,
    output: `{
  "original": "Omo Oduduwa",
  "marked": "Ọmọ Odùduwà",
  "tones": ["mid-low", "mid-low-mid-low"]
}`,
  },
  Proverbs: {
    command: `curl https://api.yoruba-api.dev/v1/proverbs/random \\
  -H "Authorization: Bearer YOUR_API_KEY"`,
    output: `{
  "yoruba": "Ẹni tó fẹ́ jẹ oyin inú àpáta...",
  "english": "He who wants to eat honey...",
  "meaning": "Great rewards require effort"
}`,
  },
};

export function TryItSection() {
  const [activeTab, setActiveTab] = useState("Translation");

  return (
    <section className="px-6 py-24" id="try-it">
      <div className="max-w-5xl mx-auto">
        <div className="text-center mb-12">
          <span className="text-sm tracking-widest text-muted-foreground">
            TRY IT OUT.
          </span>
        </div>

        {/* Terminal window */}
        <div className="bg-card border border-border overflow-hidden">
          {/* Terminal chrome */}
          <div className="flex items-center justify-between px-4 py-3 border-b border-border bg-muted/50">
            <div className="flex gap-1.5">
              <div className="w-3 h-3 rounded-full bg-red-500/60" />
              <div className="w-3 h-3 rounded-full bg-yellow-500/60" />
              <div className="w-3 h-3 rounded-full bg-green-500/60" />
            </div>
            <div className="flex gap-1">
              {tabs.map((tab) => (
                <button
                  key={tab}
                  onClick={() => setActiveTab(tab)}
                  className={`px-3 py-1 text-xs transition-colors ${
                    activeTab === tab
                      ? "bg-orange text-white"
                      : "text-muted-foreground hover:text-foreground"
                  }`}
                >
                  {tab}
                </button>
              ))}
            </div>
            <div className="w-16" />
          </div>

          {/* Terminal content */}
          <div className="p-6 font-mono text-sm">
            <div className="flex items-center gap-2 text-muted-foreground mb-2">
              <span className="text-orange">$</span>
              <span>Terminal</span>
            </div>

            {/* Command */}
            <pre className="text-muted-foreground mb-6 whitespace-pre-wrap">
              <span className="text-green-400">{">"}</span>{" "}
              {codeExamples[activeTab].command}
            </pre>

            {/* Output */}
            <div className="border-t border-border pt-4">
              <span className="text-xs text-muted-foreground mb-2 block">
                Response:
              </span>
              <pre className="text-foreground whitespace-pre-wrap">
                {codeExamples[activeTab].output}
              </pre>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
