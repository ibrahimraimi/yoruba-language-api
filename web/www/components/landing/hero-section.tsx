import { Button } from "@/components/ui/button";
import { ArrowRight, BookOpen, Github } from "lucide-react";
import { siteConfig } from "@/config/site";

export function HeroSection() {
  return (
    <section className="relative min-h-screen flex flex-col items-center justify-center px-6 py-24 overflow-hidden">
      {/* Gradient orb decoration */}
      <div className="absolute top-20 right-1/4 w-64 h-64 bg-orange/30 rounded-full blur-[120px] pointer-events-none" />
      <div className="absolute bottom-40 left-1/4 w-48 h-48 bg-gold/20 rounded-full blur-[100px] pointer-events-none" />

      <div className="max-w-4xl mx-auto text-center">
        <div className="inline-block mb-6 px-3 py-1 text-xs text-orange bg-orange/10 border border-orange/20">
          The Yoruba Language API developers love
        </div>

        <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight text-balance mb-6">
          Build excellent{" "}
          <span className="text-orange">Yoruba applications</span>, your style.
        </h1>

        <p className="text-lg text-muted-foreground max-w-2xl mx-auto mb-10 text-pretty leading-relaxed">
          Yoruba API is a{" "}
          <span className="text-foreground font-medium">REST API</span> for{" "}
          <span className="text-foreground font-medium">Developers</span>,
          combining 10,000+ curated dictionary entries with GPT-4o for
          contextually accurate translations, tone marking, and cultural wisdom.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <Button
            size="lg"
            className="bg-orange hover:bg-orange-light text-white px-6"
            asChild
          >
            <a href="/docs/installation">
              Get Started
              <ArrowRight className="ml-2 size-4" />
            </a>
          </Button>
          <Button
            variant="outline"
            size="lg"
            className="px-6 bg-transparent border-border hover:bg-muted"
            asChild
          >
            <a href="/docs">
              <BookOpen className="mr-2 size-4" />
              Documentation
            </a>
          </Button>
        </div>
      </div>

      {/* Floating code preview - Fumadocs style */}
      <div className="w-full max-w-5xl mx-auto mt-16 px-4">
        <div className="relative bg-card border border-border overflow-hidden">
          {/* Browser chrome */}
          <div className="flex items-center gap-2 px-4 py-3 border-b border-border bg-muted/50">
            <div className="flex gap-1.5">
              <div className="w-3 h-3 rounded-full bg-red-500/60" />
              <div className="w-3 h-3 rounded-full bg-yellow-500/60" />
              <div className="w-3 h-3 rounded-full bg-green-500/60" />
            </div>
            <div className="flex-1 text-center">
              <span className="text-xs text-muted-foreground">
                api.yoruba-api.dev/v1/translate
              </span>
            </div>
          </div>

          <div className="grid md:grid-cols-2 divide-x divide-border">
            {/* Request */}
            <div className="p-6">
              <div className="flex items-center gap-2 mb-4">
                <span className="px-2 py-0.5 text-xs font-medium bg-orange text-white">
                  POST
                </span>
                <span className="text-sm text-muted-foreground">
                  /translate
                </span>
              </div>
              <pre className="text-sm text-muted-foreground leading-relaxed">
                <code>
                  {`{
  "text": "Good morning",
  "source": "en",
  "target": "yo"
}`}
                </code>
              </pre>
            </div>

            {/* Response */}
            <div className="p-6 bg-muted/30">
              <div className="flex items-center gap-2 mb-4">
                <span className="px-2 py-0.5 text-xs font-medium bg-green-600 text-white">
                  200
                </span>
                <span className="text-sm text-muted-foreground">Response</span>
              </div>
              <pre className="text-sm leading-relaxed">
                <code>
                  <span className="text-muted-foreground">{"{"}</span>
                  {"\n"}
                  <span className="text-muted-foreground">
                    {"  "}
                    {'"'}translated{'"'}:{" "}
                  </span>
                  <span className="text-orange">
                    {'"'}Ẹ kú àárọ̀{'"'}
                  </span>
                  {"\n"}
                  <span className="text-muted-foreground">
                    {"  "}
                    {'"'}confidence{'"'}:{" "}
                  </span>
                  <span className="text-gold">0.95</span>
                  {"\n"}
                  <span className="text-muted-foreground">{"}"}</span>
                </code>
              </pre>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
