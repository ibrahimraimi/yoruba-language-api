import { Button } from "@/components/ui/button";
import { Github, Heart, Shield, Zap } from "lucide-react";
import { siteConfig } from "@/config/site";

export function Footer() {
  return (
    <footer className="px-6 py-24 border-t border-border">
      <div className="max-w-6xl mx-auto">
        {/* Dream Section */}
        <div className="text-center mb-16">
          <h2 className="text-2xl md:text-3xl font-bold text-gold mb-8">
            A Language of Dreams.
          </h2>

          <div className="grid md:grid-cols-2 gap-4 max-w-4xl mx-auto">
            {/* Made Possible Card */}
            <div className="bg-card border border-border p-8 text-left">
              <Heart className="size-5 text-red-500 mb-4" />
              <h3 className="text-lg font-bold mb-2">Made Possible by You.</h3>
              <p className="text-muted-foreground text-sm mb-6 leading-relaxed">
                Yoruba API is 100% powered by passion and open source community.
              </p>
              <div className="flex gap-3">
                <Button
                  size="sm"
                  className="bg-orange hover:bg-orange-light text-white"
                >
                  Sponsors
                </Button>
                <Button
                  size="sm"
                  variant="outline"
                  className="bg-transparent border-border"
                >
                  Contributors
                </Button>
              </div>
              {/* Avatar row */}
              <div className="flex mt-6 -space-x-2">
                {[...Array(8)].map((_, i) => (
                  <div
                    key={i}
                    className="w-8 h-8 rounded-full bg-muted border-2 border-card flex items-center justify-center text-xs text-muted-foreground"
                  >
                    {String.fromCharCode(65 + i)}
                  </div>
                ))}
                <div className="w-8 h-8 rounded-full bg-orange/20 border-2 border-card flex items-center justify-center text-xs text-orange">
                  +99
                </div>
              </div>
            </div>

            {/* Build Your App Card */}
            <div className="bg-card border border-border p-8 text-left relative overflow-hidden">
              <h3 className="text-sm font-bold tracking-widest text-muted-foreground mb-4">
                BUILD YOUR APP
              </h3>
              <p className="text-muted-foreground text-sm mb-6">
                Start now, for free. Join 1000+ developers.
              </p>
              {/* Decorative gradient orb */}
              <div className="absolute bottom-0 right-0 w-40 h-40 bg-gradient-to-tl from-orange/40 via-gold/20 to-transparent rounded-full blur-xl pointer-events-none" />
            </div>
          </div>
        </div>

        {/* Features row */}
        <div className="grid md:grid-cols-3 gap-6 mb-16 max-w-4xl mx-auto">
          <div className="flex items-start gap-3">
            <Shield className="size-5 text-orange shrink-0" />
            <div>
              <h4 className="font-semibold text-sm mb-1">Battery-included.</h4>
              <p className="text-muted-foreground text-xs">
                Extensible, everything useful for contributors.
              </p>
            </div>
          </div>
          <div className="flex items-start gap-3">
            <Github className="size-5 text-orange shrink-0" />
            <div>
              <h4 className="font-semibold text-sm mb-1">Fully open source.</h4>
              <p className="text-muted-foreground text-xs">
                Yoruba API is available on GitHub.
              </p>
            </div>
          </div>
          <div className="flex items-start gap-3">
            <Zap className="size-5 text-orange shrink-0" />
            <div>
              <h4 className="font-semibold text-sm mb-1">Within seconds.</h4>
              <p className="text-muted-foreground text-xs">
                Get started instantly with CLI.
              </p>
            </div>
          </div>
        </div>

        {/* CTA */}
        <div
          className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16"
          id="get-started"
        >
          <Button
            size="lg"
            className="bg-orange hover:bg-orange-light text-white px-8"
          >
            Read Docs
          </Button>
          <Button
            variant="outline"
            size="lg"
            className="px-8 bg-transparent border-border hover:bg-muted"
            asChild
          >
            <a
              href={siteConfig.links.github}
              target="_blank"
              rel="noopener noreferrer"
            >
              <Github className="mr-2 size-4" />
              Open GitHub
            </a>
          </Button>
        </div>

        {/* Bottom links */}
        <div className="flex flex-col md:flex-row items-center justify-between gap-4 pt-8 border-t border-border text-sm text-muted-foreground">
          <div className="flex items-center gap-2">
            <span className="text-orange font-bold">Yoruba</span>
            <span>API</span>
          </div>
          <p>Built with respect for the Yoruba language and its speakers.</p>
        </div>
      </div>
    </footer>
  );
}
