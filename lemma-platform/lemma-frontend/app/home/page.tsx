import type { Metadata } from 'next';
import { RootPageSwitch } from '@/components/root/root-page-switch';

export const metadata: Metadata = {
    title: 'Home | Lemma',
    robots: {
        index: false,
        follow: false,
        nocache: true,
    },
};

export default function HomeRoutePage() {
    return <RootPageSwitch mode="home" />;
}
