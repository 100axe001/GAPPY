import type { Metadata } from 'next';
import { LegalPage } from '@/components/legal/legal-page';
import { privacyPolicy } from '@/lib/data/legal';

export const metadata: Metadata = {
    title: 'Privacy Policy',
    description: privacyPolicy.description,
};

export default function PrivacyPage() {
    return <LegalPage document={privacyPolicy} />;
}
