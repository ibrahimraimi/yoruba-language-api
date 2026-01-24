import { Button } from "@/components/ui/button";
import { ExternalLink } from "lucide-react";

export function FeaturesSection() {
  return (
    <section className="px-6 py-24" id="features">
      <div className="max-w-6xl mx-auto">
        {/* Bento Grid */}
        <div className="grid md:grid-cols-2 gap-4">
          {/* Card 1: Community Love */}
          <div className="bg-card border border-border p-8 flex flex-col justify-between min-h-[280px]">
            <div>
              <h3 className="text-xl font-bold mb-3">
                A language API developers love.
              </h3>
              <p className="text-muted-foreground text-sm leading-relaxed">
                Loved by teams and developers from startups to enterprises —
                building everything from language learning apps to AI pipelines.
              </p>
            </div>
            <div className="mt-6">
              <Button
                size="sm"
                className="bg-orange hover:bg-orange-light text-white"
              >
                Examples
              </Button>
            </div>
          </div>

          {/* Card 2: Testimonial */}
          <div className="bg-card border border-border p-6 flex flex-col">
            <div className="flex-1 p-4 bg-muted/50 border border-border mb-4">
              <p className="text-sm text-muted-foreground leading-relaxed">
                {
                  '"You know how you end up rebuilding a full translation layer every time you start a new project?'
                }
              </p>
              <p className="text-sm text-foreground mt-3 leading-relaxed">
                Yoruba API fixes this by giving you all the right primitives out
                of the box.
              </p>
              <p className="text-sm text-muted-foreground mt-3">
                {'"Use headless endpoints to build exactly what you need."'}
              </p>
            </div>
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded-full bg-orange/20 flex items-center justify-center text-orange text-xs font-bold">
                AD
              </div>
              <div>
                <div className="text-sm font-medium">Adéọlá</div>
                <div className="text-xs text-muted-foreground">
                  Creator of YorubaLearn
                </div>
              </div>
            </div>
          </div>

          {/* Card 3: Code Preview */}
          <div className="bg-card border border-border p-0 overflow-hidden">
            <div className="flex items-center gap-2 px-4 py-3 border-b border-border bg-muted/50">
              <div className="flex gap-1.5">
                <div className="w-2.5 h-2.5 rounded-full bg-red-500/60" />
                <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/60" />
                <div className="w-2.5 h-2.5 rounded-full bg-green-500/60" />
              </div>
              <span className="text-xs text-muted-foreground ml-2">
                Quick Start
              </span>
            </div>
            <div className="p-6 font-mono text-sm">
              <div className="text-muted-foreground">
                <span className="text-orange">const</span> yoruba ={" "}
                <span className="text-orange">new</span>{" "}
                <span className="text-gold">YorubaAPI</span>(apiKey);
              </div>
              <div className="text-muted-foreground mt-2">
                <span className="text-orange">const</span> result ={" "}
                <span className="text-orange">await</span> yoruba.
                <span className="text-gold">translate</span>({"{"}
              </div>
              <div className="text-muted-foreground ml-4">
                text: <span className="text-green-400">{'"Hello"'}</span>,
              </div>
              <div className="text-muted-foreground ml-4">
                target: <span className="text-green-400">{'"yo"'}</span>
              </div>
              <div className="text-muted-foreground">{"}"});</div>
              <div className="mt-4 pt-4 border-t border-border">
                <Button
                  size="sm"
                  variant="outline"
                  className="bg-transparent text-orange border-orange/30 hover:bg-orange/10"
                >
                  Docs
                </Button>
              </div>
            </div>
          </div>

          {/* Card 4: Customization */}
          <div className="bg-card border border-border p-8">
            <h3 className="text-xl font-bold mb-3">
              Minimal footprint. Maximum flexibility.
            </h3>
            <p className="text-muted-foreground text-sm leading-relaxed mb-6">
              Yoruba API offers well-designed endpoints, with a headless mode to
              plug into your own UI.
            </p>
            <p className="text-muted-foreground text-sm mb-4">
              Pro developer? Customize the responses using query parameters:
            </p>
            <code className="text-sm text-orange bg-orange/10 px-3 py-1.5 block">
              ?include=transliteration,audio,examples
            </code>
          </div>
        </div>
      </div>
    </section>
  );
}
