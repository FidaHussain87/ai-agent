'use client'

import Link from 'next/link'
import { usePathname, useRouter } from 'next/navigation'

export default function Navbar() {
  const router = useRouter()
  const pathname = usePathname()

  const logout = () => {
    localStorage.removeItem('token')
    router.push('/login')
  }

  return (
    <nav className="flex items-center justify-between p-4 bg-gray-900 text-white">
      <div className="flex gap-6">
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/dashboard/agents">Agents</Link>
        <Link href="/dashboard/pipelines">Pipelines</Link>
        <Link href="/dashboard/metrics">Metrics</Link>
      </div>
      <div className="flex items-center gap-4">
        <span className="text-sm">{pathname.replace('/dashboard/', '').toUpperCase()}</span>
        <button onClick={logout} className="px-3 py-1 bg-red-500 rounded">Logout</button>
      </div>
    </nav>
  )
}
