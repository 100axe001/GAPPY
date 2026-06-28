import { Sparkles } from "lucide-react";

import { Logo } from "@/components/brand/logo";
import { Button } from "@/components/ui/button";

import { SETUP_STEPS, type SetupStep } from "./account-onboarding-helpers";

export function SetupShell({ children }: { children: React.ReactNode }) {
  return (
    <main className="setup-theme-light setup-shell relative flex min-h-screen items-center justify-center overflow-hidden px-4 py-8 text-[var(--text-primary)]">
      <div className="setup-shell-bottom-glow absolute inset-x-0 bottom-0 h-72" />
      <div className="setup-shell-rail absolute inset-0" />
      <div className="relative flex w-full items-center justify-center">
        {children}
      </div>
    </main>
  );
}

export function SetupChrome({ intro = false }: { intro?: boolean }) {
  return (
    <header
      className={[
        "flex items-center justify-between",
        intro ? "setup-chrome-intro" : "",
      ].join(" ")}
    >
      <Logo size="sm" className="text-[var(--text-primary)]" />
      <div className="setup-badge rounded-full px-3 py-1 text-xs font-medium">
        Setup
      </div>
    </header>
  );
}

export function SetupPanel({
  title,
  subtitle,
  children,
  titleClassName = "",
  subtitleClassName = "",
}: {
  title: string;
  subtitle?: string;
  children: React.ReactNode;
  titleClassName?: string;
  subtitleClassName?: string;
}) {
  return (
    <div className="w-full text-center">
      <h1
        className={[
          "setup-panel-title mx-auto max-w-4xl font-normal tracking-normal text-[var(--text-primary)]",
          titleClassName,
        ].join(" ")}
      >
        {title}
      </h1>
      {subtitle ? (
        <p
          className={[
            "mx-auto mt-3 max-w-2xl text-base leading-7 text-[var(--text-secondary)]",
            subtitleClassName,
          ].join(" ")}
        >
          {subtitle}
        </p>
      ) : null}
      {children}
    </div>
  );
}

export function SetupPrimaryButton({
  children,
  className = "",
  ...props
}: React.ComponentProps<typeof Button>) {
  return (
    <Button
      {...props}
      className={[
        "setup-primary-action !flex mx-auto mt-8 h-12 min-w-56 gap-3 px-7 text-sm font-medium",
        className,
      ].join(" ")}
    >
      <Sparkles className="h-5 w-5" />
      {children}
    </Button>
  );
}

export function ProgressDots({
  currentStep,
  steps = SETUP_STEPS,
}: {
  currentStep: SetupStep;
  steps?: SetupStep[];
}) {
  const currentIndex = steps.indexOf(currentStep);
  return (
    <div
      className={[
        "absolute bottom-7 left-1/2 flex -translate-x-1/2 gap-3",
        currentStep === "boot" ? "setup-boot-progress" : "",
      ].join(" ")}
    >
      {steps.map((step, index) => (
        <span
          key={step}
          className={[
            "setup-progress-dot h-2 w-2 transition",
            index === currentIndex
              ? "is-active"
              : index < currentIndex
                ? "is-complete"
                : "",
          ].join(" ")}
        />
      ))}
    </div>
  );
}
