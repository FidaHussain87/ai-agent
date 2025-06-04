'use client'

import { useEffect, useState } from 'react'
import api from '@/utils/api'

export default function MetricsPage() {
  const [metrics, setMetrics] = useState([])

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const res = await api.get('/metrics/agent/1') // replace with dynamic agent_id if needed
        setMetrics(res.data)
      } catch (err) {
        console.error('Failed to fetch metrics', err)
      }
    }
    fetchMetrics()
  }, [])

  return (
    <div className="p-4">
      <h2 className="text-xl font-semibold mb-4">Agent Metrics</h2>
      <table className="min-w-full table-auto text-sm">
        <thead>
          <tr>
            <th className="px-2 py-1">Confidence</th>
            <th className="px-2 py-1">Duration (s)</th>
            <th className="px-2 py-1">Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {metrics.map((metric: any) => (
            <tr key={metric.id}>
              <td className="border px-2 py-1">{metric.confidence}</td>
              <td className="border px-2 py-1">{metric.execution_time}</td>
              <td className="border px-2 py-1">{metric.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
