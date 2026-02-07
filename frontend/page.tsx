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
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        {/* Connection Status Card */}
        <div className="md:col-span-1 space-y-6">
          <div className="p-6 rounded-2xl bg-zinc-900 border border-zinc-800">
            <h2 className="text-sm font-semibold text-zinc-400 mb-4 uppercase tracking-wider">Integrations</h2>
            <div className="space-y-4">
              <div className="flex justify-between items-center">
                <span className="text-zinc-200">GitHub</span>
                <span className="text-green-500 text-xs">CONNECTED</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-zinc-200">Search Console</span>
                <span className="text-yellow-500 text-xs">LINKED (PROTOTYPE)</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-zinc-200">Telegram Bot</span>
                <span className="text-green-500 text-xs">ACTIVE</span>
              </div>
            </div>
            <button className="w-full mt-6 py-2 bg-white text-black rounded-lg font-bold text-sm hover:bg-zinc-200 transition-colors">
              SYNC ALL DATA
            </button>
          </div>
        </div>

        {/* Main Stats/Actions */}
        <div className="md:col-span-2 space-y-6">
          <div className="p-8 rounded-2xl bg-zinc-900 border border-zinc-800 relative overflow-hidden">
            <div className="relative z-10">
              <h2 className="text-lg font-bold mb-2">Autonomous Agent Status</h2>
              <p className="text-zinc-400 mb-6 italic">"Currently scanning trialmoltbot-repo for striking distance keywords..."</p>
              
              <div className="space-y-4">
                <div className="p-4 rounded-xl bg-black border border-zinc-800 flex justify-between items-center">
                  <div>
                    <h3 className="text-sm font-bold">SEO Audit Found 3 Opportunities</h3>
                    <p className="text-xs text-zinc-500">High impact changes detected for Page 2 keywords.</p>
                  </div>
                  <button className="px-4 py-2 bg-zinc-800 rounded-lg text-xs font-bold hover:bg-zinc-700">VIEW IN TELEGRAM</button>
                </div>
              </div>
            </div>
          </div>

          {/* Recent Activity */}
          <div className="p-6 rounded-2xl bg-zinc-900 border border-zinc-800">
            <h2 className="text-sm font-semibold text-zinc-400 mb-4 uppercase tracking-wider">Recent Vibecodes</h2>
            <div className="space-y-4">
              <div className="flex gap-4 items-start border-l-2 border-zinc-800 pl-4">
                <div className="flex-1">
                  <p className="text-sm text-zinc-200 font-medium">Pushed SEO fix for 'ai automation'</p>
                  <p className="text-xs text-zinc-500">24 mins ago • divygoyal/trialmoltbot</p>
                </div>
              </div>
              <div className="flex gap-4 items-start border-l-2 border-zinc-800 pl-4 opacity-50">
                <div className="flex-1">
                  <p className="text-sm text-zinc-200 font-medium">Initialized repo structure</p>
                  <p className="text-xs text-zinc-500">1 hour ago • divygoyal/trialmoltbot</p>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </main>
  );
}
