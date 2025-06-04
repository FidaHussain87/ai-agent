'use client'

import { useEffect, useState } from 'react'
import api from '@/utils/api'

export default function AgentDashboard() {
  const [agents, setAgents] = useState([])

  useEffect(() => {
    const fetchAgents = async () => {
      try {
        const res = await api.get('/agents')
        setAgents(res.data)
      } catch (err) {
        console.error('Failed to fetch agents', err)
      }
    }
    fetchAgents()
  }, [])

  return (
    <div className="p-4">
      <h2 className="text-xl font-semibold mb-4">Your Agents</h2>
      <ul className="space-y-2">
        {agents.map((agent: any) => (
          <li key={agent.id} className="p-4 bg-gray-100 rounded shadow">
            <strong>{agent.name}</strong> — {agent.task_type}
          </li>
        ))}
      </ul>
    </div>
  )
}
