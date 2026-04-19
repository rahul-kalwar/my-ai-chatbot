import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Perplexity 2.0",
  description: "AI Chat with web search",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}