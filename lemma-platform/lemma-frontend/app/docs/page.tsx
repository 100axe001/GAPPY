import type { Metadata } from 'next';
import { DocsHome } from '@/components/docs/docs-shell';

export const metadata: Metadata = {
  title: 'Documentation',
  description: 'Learn the Lemma platform, SDK, and CLI.',
  openGraph: {
    title: 'Lemma Documentation',
    description: 'Learn the Lemma platform, SDK, and CLI.',
    type: 'website',
  },
};

export default function DocsPage() {
  return <DocsHome />;
}
