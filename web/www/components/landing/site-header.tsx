"use client";

import { RiGithubLine } from "@remixicon/react";

import { cn } from "@/lib/utils";
import { siteConfig } from "@/config/site";
import { useScroll } from "@/hooks/use-scroll";

export function SiteHeader() {
  const scrolled = useScroll(10);
  return (
    <header
      className={cn(
        "sticky top-0 z-50 w-full py-2 border-transparent border-b",
        {
          "border-border bg-background/95 backdrop-blur-sm supports-backdrop-filter:bg-background/50":
            scrolled,
        },
      )}
    >
      <nav className="mx-auto flex h-14 w-full max-w-7xl items-center justify-between">
        <div className="flex items-center gap-2">
          <span className="text-orange font-bold">Yoruba</span>
          <span className="text-muted-foreground">API</span>
        </div>
        <div className="flex items-center gap-6 text-sm text-muted-foreground">
          <a
            href="#documentation"
            className="hover:text-foreground transition-colors"
          >
            Documentation
          </a>
          <a
            href="#features"
            className="hover:text-foreground transition-colors"
          >
            Features
          </a>
          <a
            href={siteConfig.links.github}
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-foreground transition-colors"
          >
            <RiGithubLine className="size-4" />
          </a>
        </div>
      </nav>
    </header>
  );
}
