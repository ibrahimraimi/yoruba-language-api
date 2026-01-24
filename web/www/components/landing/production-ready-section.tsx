import { Button } from "@/components/ui/button";
import { Server, Database, Zap, Code2, Search, Blocks } from "lucide-react";

const features = [
  {
    icon: Server,
    title: "Production Ready Architecture.",
    description:
      "FastAPI backend, PostgreSQL data store, and Kubernetes-ready manifests for scaling.",
    badges: ["FastAPI", "PostgreSQL", "K8s"],
  },
  {
    icon: Blocks,
    title: "AI & Dictionary Hybrid.",
    description:
      "Seamless integration of 10,000+ dictionary entries with GPT-4o intelligence.",
    items: [
      { name: "yoruba-db", desc: "Curated linguistic database" },
      {
        name: "yoruba-ai",
        desc: "Context-aware AI translation layer",
      },
      { name: "yoruba-tone", desc: "Advanced tone marking service" },
    ],
  },
  {
    icon: Database,
    title: "Modern Tech Stack.",
    description:
      "Built with performance in mind using Redis for caching and Docker for orchestration.",
    badges: ["Docker", "Redis", "GitHub Actions"],
  },
  {
    icon: Code2,
    title: "Developer First.",
    description:
      "Clean, well-documented REST endpoints. No complex setup—just pure JSON.",
    showPreview: true,
  },
  {
    icon: Search,
    title: "Enhance your search experience.",
    description:
      "Integrate with Orama Search and Algolia Search in your Yoruba apps easily.",
  },
  {
    icon: Zap,
    title: "Tone & Culture.",
    description:
      "Automatic tone marking and random proverbs retrieval for rich cultural context.",
  },
];

export function ProductionReadySection() {
  return (
    <section className="px-6 py-24" id="documentation">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-2xl md:text-3xl font-bold text-gold mb-4">
            Built For Engineers.
          </h2>
        </div>

        {/* Bento Grid */}
        <div className="grid md:grid-cols-2 gap-4">
          {/* Card 1: Framework Agnostic */}
          <div className="bg-card border border-border p-8">
            <Server className="size-5 text-orange mb-4" />
            <h3 className="text-lg font-bold mb-2">{features[0].title}</h3>
            <p className="text-muted-foreground text-sm mb-4 leading-relaxed">
              {features[0].description}
            </p>
            {features[0].badges && (
              <div className="flex gap-2">
                {features[0].badges.map((badge) => (
                  <span
                    key={badge}
                    className="px-2 py-1 text-xs bg-muted text-muted-foreground"
                  >
                    {badge}
                  </span>
                ))}
              </div>
            )}
          </div>

          {/* Card 2: Composable */}
          <div className="bg-card border border-border p-8">
            <Blocks className="size-5 text-orange mb-4" />
            <h3 className="text-lg font-bold mb-2">{features[1].title}</h3>
            <p className="text-muted-foreground text-sm mb-4 leading-relaxed">
              {features[1].description}
            </p>
            {features[1].items && (
              <div className="space-y-2">
                {features[1].items.map((item) => (
                  <div
                    key={item.name}
                    className="flex items-center justify-between text-xs"
                  >
                    <span className="text-orange font-mono">{item.name}</span>
                    <span className="text-muted-foreground">{item.desc}</span>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Card 3: Content Sources */}
          <div className="bg-card border border-border p-8">
            <Database className="size-5 text-orange mb-4" />
            <h3 className="text-lg font-bold mb-2">{features[2].title}</h3>
            <p className="text-muted-foreground text-sm mb-4 leading-relaxed">
              {features[2].description}
            </p>
            {features[2].badges && (
              <div className="flex flex-wrap gap-2">
                {features[2].badges.map((badge) => (
                  <span
                    key={badge}
                    className="px-2 py-1 text-xs bg-orange/10 text-orange border border-orange/20"
                  >
                    {badge}
                  </span>
                ))}
              </div>
            )}
          </div>

          {/* Card 4: No CMS Preview */}
          <div className="bg-card border border-border p-0 overflow-hidden">
            <div className="p-6 pb-0">
              <Code2 className="size-5 text-orange mb-4" />
              <h3 className="text-lg font-bold mb-2">{features[3].title}</h3>
              <p className="text-muted-foreground text-sm leading-relaxed">
                {features[3].description}
              </p>
            </div>
            {features[3].showPreview && (
              <div className="mt-4 p-4 bg-muted/30 border-t border-border">
                <div className="flex items-center gap-2 text-xs text-muted-foreground mb-2">
                  <span className="w-2 h-2 rounded-full bg-orange" />
                  API Page
                </div>
                <div className="text-xs text-muted-foreground">
                  <span className="text-foreground">API Status</span>
                  <br />
                  <span className="ml-4 text-muted-foreground/60">
                    service: healthy
                  </span>
                </div>
              </div>
            )}
          </div>

          {/* Card 5: Search */}
          <div className="bg-card border border-border p-8">
            <Search className="size-5 text-orange mb-4" />
            <h3 className="text-lg font-bold mb-2">{features[4].title}</h3>
            <p className="text-muted-foreground text-sm mb-4 leading-relaxed">
              {features[4].description}
            </p>
            <Button
              size="sm"
              className="bg-orange hover:bg-orange-light text-white"
            >
              Learn More
            </Button>
          </div>

          {/* Card 6: UI Components */}
          <div className="bg-card border border-border p-8 relative overflow-hidden">
            <Zap className="size-5 text-orange mb-4" />
            <h3 className="text-lg font-bold mb-2">{features[5].title}</h3>
            <p className="text-muted-foreground text-sm mb-4 leading-relaxed">
              {features[5].description}
            </p>
            <Button
              size="sm"
              className="bg-orange hover:bg-orange-light text-white"
            >
              Components
            </Button>
            {/* Decorative gradient */}
            <div className="absolute bottom-0 right-0 w-32 h-32 bg-linear-to-tl from-orange/40 via-gold/20 to-transparent rounded-full blur-xl pointer-events-none" />
          </div>
        </div>
      </div>
    </section>
  );
}
