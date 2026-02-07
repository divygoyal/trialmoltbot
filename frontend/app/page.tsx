import React from 'react';

export default function Dashboard() {
  return (
    <main className="min-h-screen p-8 max-w-6xl mx-auto">
      {/* Header */}
      <header className="flex justify-between items-center mb-12 border-b border-zinc-800 pb-6">
        <div>
          <h1 className="text-2xl font-bold tracking-tighter text-white">TRIAL MOLT BOT</h1>
          <p className="text-zinc-400 text-sm">Autonomous SEO Command Center</p>
        </div>
        <div className="flex gap-4">
          <div className="px-3 py-1 rounded-full bg-green-500/10 text-green-500 text-xs font-medium border border-green-500/20 flex items-center gap-2">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
            </span>
            JARVIS ONLINE
          </div>
        </div>
      </header>

      {/* Grid Layout */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
        
        {/* Step 1: Auth */}
        <div className="space-y-6">
          <div className="p-8 rounded-3xl bg-zinc-900 border border-zinc-800 hover:border-zinc-700 transition-all">
            <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center mb-6">
              <span className="text-black font-bold">1</span>
            </div>
            <h2 className="text-xl font-bold mb-2">Connect GitHub</h2>
            <p className="text-zinc-400 mb-8">Grant Jarvis permission to code directly in your repositories.</p>
            <a href="http://localhost:8000/login" className="inline-block w-full py-4 bg-white text-black rounded-xl font-bold text-center hover:scale-[1.02] active:scale-[0.98] transition-all">
              LOGIN WITH GITHUB
            </a>
          </div>
        </div>

        {/* Step 2: Telegram */}
        <div className="space-y-6">
          <div className="p-8 rounded-3xl bg-zinc-900 border border-zinc-800 hover:border-zinc-700 transition-all">
            <div className="w-12 h-12 bg-zinc-800 rounded-full flex items-center justify-center mb-6">
              <span className="text-white font-bold">2</span>
            </div>
            <h2 className="text-xl font-bold mb-2">Sync Telegram</h2>
            <p className="text-zinc-400 mb-8">Link your account to the bot to start coding with your voice or text.</p>
            <a href="https://t.me/trialmoltbot" target="_blank" className="inline-block w-full py-4 bg-zinc-800 text-white rounded-xl font-bold text-center border border-zinc-700 hover:bg-zinc-700 transition-all">
              OPEN TELEGRAM BOT
            </a>
          </div>
        </div>

      </div>

      <div className="mt-20 text-center">
        <p className="text-zinc-600 text-sm">Trial Molt Bot v1.0 • Built for the God Vision</p>
      </div>

    </main>
  );
}
