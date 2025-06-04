
'use client'
import { useState } from 'react'
import api from '@/utils/api'
import { useRouter } from 'next/navigation'

export default function RegisterPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const router = useRouter()

  const register = async () => {
    try {
      await api.post('/auth/register', { email, password })
      router.push('/login')
    } catch (err) {
      alert('Registration failed')
    }
  }

  return (
    <main className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Register</h1>
      <input placeholder="Email" className="input" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input placeholder="Password" type="password" className="input mt-2" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={register} className="btn mt-4">Register</button>
    </main>
  )
}
