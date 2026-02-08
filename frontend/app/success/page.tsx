'use client';

import React, { Suspense } from 'react';
import { useSearchParams } from 'next/navigation';
import { CheckCircle, MessageSquare, Copy, ExternalLink } from 'lucide-react';

function SuccessContent() {
  const searchParams = useSearchParams();
  const code = searchParams.get('code') || 'XXXX';

  const copyToClipboard = () => {
    navigator.clipboard.writeText(`/connect ${code}`);
    alert('Command copied! Now paste it in the Telegram Bot.');
  };

  return (
    <main className="min-h-screen bg-black text-white flex items-center justify-center p-6">
      <div className="max-w-md w-full">
        {/* Animated Background Glow */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>

        <div className="relative z-10 bg-zinc-900 border border-zinc-800 rounded-3xl p-8 text-center">
          <div className="w-16 h-16 bg-green-500/10 rounded-full flex items-center justify-center mx-auto mb-6">
            <CheckCircle className="text-green-500 w-8 h-8" />
          </div>

          <h1 className="text-2xl font-bold mb-2 tracking-tight">GitHub Connected!</h1>
          <p className="text-zinc-400 text-sm mb-8">Your account is authorized. Now link it to your Telegram bot to start vibecoding.</p>

          <div className="bg-black rounded-2xl p-6 border border-zinc-800 mb-8 group relative">
            <p className="text-xs text-zinc-500 uppercase tracking-widest font-bold mb-2">Your Connection Code</p>
            <div className="text-4xl font-mono font-black tracking-[0.2em] text-white py-2">
              {code}
            </div>
            <button 
              onClick={copyToClipboard}
              className="absolute top-4 right-4 text-zinc-500 hover:text-white transition-colors"
            >
              <Copy size={18} />
            </button>
          </div>

          <div className="space-y-4">
            <button 
              onClick={copyToClipboard}
              className="w-full py-4 bg-white text-black rounded-xl font-bold flex items-center justify-center gap-2 hover:scale-[1.02] active:scale-[0.98] transition-all"
            >
              COPY /CONNECT COMMAND
            </button>
            
            <a 
              href="https://t.me/trialmoltbot" 
              target="_blank"
              className="w-full py-4 bg-zinc-800 text-white rounded-xl font-bold flex items-center justify-center gap-2 hover:bg-zinc-700 transition-all"
            >
              OPEN TELEGRAM BOT <ExternalLink size={18} />
            </a>
          </div>

          <p className="mt-8 text-xs text-zinc-600">
            Paste the command in the chat to activate your autonomous engineer.
          </p>
        </div>
      </div>
    </main>
  );
}

export default function SuccessPage() {
  return (
    <Suspense fallback={<div className="min-h-screen bg-black flex items-center justify-center text-white">Loading...</div>}>
      <SuccessContent />
    </Suspense>
  );
}
