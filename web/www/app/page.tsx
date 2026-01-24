import { HeroSection } from "@/components/landing/hero-section";
import { TryItSection } from "@/components/landing/try-it-section";
import { FeaturesSection } from "@/components/landing/features-section";
import { UseCasesSection } from "@/components/landing/use-cases-section";
import { ProductionReadySection } from "@/components/landing/production-ready-section";
import { Footer } from "@/components/landing/footer";

export default function Home() {
  return (
    <main className="min-h-screen">
      <HeroSection />
      <TryItSection />
      <FeaturesSection />
      <UseCasesSection />
      <ProductionReadySection />
      <Footer />
    </main>
  );
}
