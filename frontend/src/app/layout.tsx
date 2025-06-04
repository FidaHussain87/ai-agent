'use client'
import '@/styles/global.css'
import { ReactNode } from 'react'
import Navbar from '@/components/Navbar'

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <div className="max-w-6xl mx-auto p-4">{children}</div>
      </body>
    </html>
  )
}
