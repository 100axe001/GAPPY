import type { Metadata } from 'next';
import { notFound, redirect } from 'next/navigation';
import { DocsPageView } from '@/components/docs/docs-shell';
import { docsPages, getDocsPageFromSegments } from '@/lib/data/docs';

type DocsRouteProps = {
  params: Promise<{
    slug?: string[];
  }>;
};

export function generateStaticParams() {
  return docsPages.map((page) => ({
    slug: page.slug.split('/'),
  }));
}

export async function generateMetadata({ params }: DocsRouteProps): Promise<Metadata> {
  const { slug } = await params;
  const groupRoot = getGroupRootRedirect(slug);
  if (groupRoot) {
    const page = getDocsPageFromSegments(groupRoot.split('/'));
    return {
      title: page ? `${page.title} Documentation` : 'Documentation',
      description: page?.description,
    };
  }

  const page = getDocsPageFromSegments(slug);

  if (!page) {
    return {
      title: 'Documentation',
    };
  }

  return {
    title: `${page.title} Documentation`,
    description: page.description,
    openGraph: {
      title: `${page.title} | Lemma Docs`,
      description: page.description,
      type: 'article',
    },
  };
}

export default async function DocsRoute({ params }: DocsRouteProps) {
  const { slug } = await params;
  const groupRoot = getGroupRootRedirect(slug);
  if (groupRoot) {
    redirect(`/docs/${groupRoot}`);
  }

  const page = getDocsPageFromSegments(slug);

  if (!page) {
    notFound();
  }

  if (page.slug === 'overview') {
    redirect('/docs');
  }

  return <DocsPageView page={page} />;
}

function getGroupRootRedirect(slug?: string[]): string | null {
  const value = slug?.join('/');
  if (value === 'platform') return 'platform/missions-and-pods';
  if (value === 'sdk') return 'sdk/installation';
  if (value === 'cli') return 'cli/overview';
  if (value === 'guides') return 'guides/build-a-app';
  if (value === 'reference') return 'reference/commands';
  return null;
}
