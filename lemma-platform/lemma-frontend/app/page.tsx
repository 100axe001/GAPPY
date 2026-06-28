import type { Metadata } from 'next';
import { RootPageSwitch } from '@/components/root/root-page-switch';

export const metadata: Metadata = {
    title: 'Company Systems That Actually Run',
    description:
        'Lemma is where your company\'s real work lives: agents, data, automations, and team interfaces all inside one pod.',
    robots: {
        index: true,
        follow: true,
    },
    openGraph: {
        title: 'Lemma | Company Systems That Actually Run',
        description:
            'Lemma is where your company\'s real work lives: agents, data, automations, and team interfaces all inside one pod.',
        type: 'website',
    },
    twitter: {
        card: 'summary',
        title: 'Lemma | Company Systems That Actually Run',
        description:
            'Lemma is where your company\'s real work lives: agents, data, automations, and team interfaces all inside one pod.',
    },
};

export default function HomePage() {
    return <RootPageSwitch />;
}
