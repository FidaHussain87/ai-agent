'use client'

export default function DashboardHome() {
    console.log('Dashboard Home Loaded')
  return (
    <div className="p-4">
      <h1 className="text-3xl font-bold mb-4">Welcome to your Dashboard</h1>
      <p className="text-gray-600">Use the navigation to manage agents, pipelines, and metrics.</p>
    </div>
  )
}
