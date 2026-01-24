"use client";

import { useState } from "react";
import { Check } from "lucide-react";

const tabs = ["Developer", "Researcher", "EdTech"];

const useCaseContent: Record<
  string,
  { title: string; description: string; features: string[] }
> = {
  Developer: {
    title: "The familiar REST API.",
    description:
      "It is just REST, with additional features seamlessly integrated into the endpoints.",
    features: [
      "JSON responses with consistent schemas",
      "Comprehensive error handling",
      "Rate limiting and caching built-in",
      "SDKs for Python, JavaScript, Go",
      "Webhook support for async operations",
    ],
  },
  Researcher: {
    title: "Built for linguistic research.",
    description:
      "Access structured datasets perfect for NLP research and linguistic analysis.",
    features: [
      "Phonetic transcriptions included",
      "Morphological breakdowns",
      "Etymology and word origins",
      "Dialect variations noted",
      "Export to common research formats",
    ],
  },
  EdTech: {
    title: "Perfect for learning apps.",
    description:
      "All the building blocks for creating engaging Yoruba learning experiences.",
    features: [
      "Audio pronunciations available",
      "Difficulty levels for vocabulary",
      "Contextual example sentences",
      "Quiz and assessment endpoints",
      "Progress tracking helpers",
    ],
  },
};

export function UseCasesSection() {
  const [activeTab, setActiveTab] = useState("Developer");
  const content = useCaseContent[activeTab];

  return (
    <section className="px-6 py-24" id="use-cases">
      <div className="max-w-5xl mx-auto">
        <div className="text-center mb-12">
          <h2 className="text-2xl md:text-3xl font-bold text-gold mb-4">
            Solving real linguistic challenges.
          </h2>
          <p className="text-muted-foreground max-w-xl mx-auto">
            Providing the technical foundation for preservation, study, and
            practical application of the Yoruba language.
          </p>
        </div>

        {/* Tabs */}
        <div className="flex items-center justify-center gap-4 mb-12">
          {tabs.map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-4 py-2 text-sm transition-colors ${
                activeTab === tab
                  ? "text-foreground border-b-2 border-orange"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              {tab}
            </button>
          ))}
        </div>

        {/* Content */}
        <div className="grid md:grid-cols-2 gap-8 items-start">
          {/* Code preview */}
          <div className="bg-card border border-border overflow-hidden">
            <div className="flex items-center gap-2 px-4 py-3 border-b border-border bg-muted/50">
              <div className="flex gap-1.5">
                <div className="w-2.5 h-2.5 rounded-full bg-red-500/60" />
                <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/60" />
                <div className="w-2.5 h-2.5 rounded-full bg-green-500/60" />
              </div>
              <span className="text-xs text-muted-foreground ml-2">
                example.js
              </span>
            </div>
            <div className="p-6 font-mono text-sm">
              <div className="text-muted-foreground">
                <span className="text-orange">import</span> {"{ YorubaAPI }"}{" "}
                <span className="text-orange">from</span>{" "}
                <span className="text-green-400">{'"@yoruba-api/sdk"'}</span>
              </div>
              <div className="text-muted-foreground mt-4">
                <span className="text-orange">const</span> api ={" "}
                <span className="text-orange">new</span>{" "}
                <span className="text-gold">YorubaAPI</span>()
              </div>
              <div className="text-muted-foreground mt-4">
                <span className="text-purple-400">{"// "}</span>
                <span className="text-muted-foreground/60">
                  {content.title}
                </span>
              </div>
              <div className="text-muted-foreground mt-2">
                <span className="text-orange">const</span> result ={" "}
                <span className="text-orange">await</span> api.
                <span className="text-gold">query</span>({"{"}
              </div>
              <div className="text-muted-foreground ml-4">
                endpoint:{" "}
                <span className="text-green-400">{'"translate"'}</span>,
              </div>
              <div className="text-muted-foreground ml-4">
                options: {"{ "}includeAudio:{" "}
                <span className="text-orange">true</span>
                {" }"}
              </div>
              <div className="text-muted-foreground">{"}"});</div>
            </div>
          </div>

          {/* Features list */}
          <div>
            <h3 className="text-xl font-bold mb-2">{content.title}</h3>
            <p className="text-muted-foreground text-sm mb-6">
              {content.description}
            </p>
            <ul className="space-y-3">
              {content.features.map((feature) => (
                <li
                  key={feature}
                  className="flex items-start gap-3 text-sm text-muted-foreground"
                >
                  <Check className="size-4 text-orange shrink-0 mt-0.5" />
                  {feature}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}
