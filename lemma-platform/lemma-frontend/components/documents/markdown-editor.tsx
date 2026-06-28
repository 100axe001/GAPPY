'use client';

import { useEditor, EditorContent, type Editor } from '@tiptap/react';
import StarterKit from '@tiptap/starter-kit';
import Placeholder from '@tiptap/extension-placeholder';
import { Table, TableCell, TableHeader, TableRow } from '@tiptap/extension-table';
import { useEffect, useRef } from 'react';
import { cn } from '@/lib/utils';
import { Markdown } from 'tiptap-markdown';

type MarkdownEnabledEditor = Editor & {
    storage: {
        markdown: {
            getMarkdown: () => string;
        };
    };
};

interface MarkdownEditorProps {
    content: string;
    onChange: (content: string) => void;
    editable?: boolean;
    className?: string;
    editorClassName?: string;
    placeholder?: string;
    onSubmitShortcut?: () => void;
    readableProse?: boolean;
}

export function MarkdownEditor({
    content,
    onChange,
    editable = true,
    className,
    editorClassName,
    placeholder = 'Start writing...',
    onSubmitShortcut,
    readableProse = false,
}: MarkdownEditorProps) {
    const lastEmittedMarkdownRef = useRef(content);

    const getMarkdown = (editor: Editor) => {
        return (editor as MarkdownEnabledEditor).storage.markdown.getMarkdown();
    };

    const editor = useEditor({
        extensions: [
            StarterKit,
            Table.configure({
                resizable: true,
                HTMLAttributes: {
                    class: 'lemma-markdown-table my-4 w-full border-collapse text-sm',
                },
            }),
            TableRow,
            TableHeader.configure({
                HTMLAttributes: {
                    class: 'border border-[var(--border-subtle)] bg-[var(--surface-2)] px-3 py-2 text-left text-xs font-semibold text-[var(--text-primary)]',
                },
            }),
            TableCell.configure({
                HTMLAttributes: {
                    class: 'border border-[var(--border-subtle)] px-3 py-2 align-top',
                },
            }),
            Placeholder.configure({
                placeholder,
            }),
            Markdown.configure({
                html: false,
                transformPastedText: true,
                transformCopiedText: true,
            })
        ],
        content,
        editable,
        editorProps: {
            attributes: {
                class: cn(
                    'tiptap-editor prose prose-neutral dark:prose-invert min-h-[200px] text-[var(--text-primary)] focus:outline-none',
                    readableProse ? 'lemma-markdown-editor' : 'max-w-none',
                    editorClassName
                ),
            },
            handleKeyDown: (_view, event) => {
                if (onSubmitShortcut && (event.metaKey || event.ctrlKey) && event.key === 'Enter') {
                    event.preventDefault();
                    onSubmitShortcut();
                    return true;
                }

                return false;
            },
        },
        onUpdate: ({ editor, transaction }) => {
            if (!transaction.docChanged || !editor.isFocused) {
                return;
            }
            const markdown = getMarkdown(editor);
            lastEmittedMarkdownRef.current = markdown;
            onChange(markdown);
        },
        immediatelyRender: false,
    });

    useEffect(() => {
        if (!editor) return;

        const currentMarkdown = getMarkdown(editor);
        if (content === currentMarkdown || content === lastEmittedMarkdownRef.current) {
            return;
        }

        editor.commands.setContent(content);
        lastEmittedMarkdownRef.current = content;
    }, [content, editor]);

    useEffect(() => {
        if (editor) {
            editor.setEditable(editable);
        }
    }, [editable, editor]);

    if (!editor) {
        return null;
    }

    return (
        <div className={cn("relative min-h-[200px]", className)}>
            <EditorContent editor={editor} />
        </div>
    );
}
