'use client';
import { useState } from 'react';
import api from '@/utils/api';
import { useRouter } from 'next/navigation';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleLogin = async () => {
    try {
      await api.post(
        '/auth/login',
        new URLSearchParams({ username: email, password }),
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            withCredentials: true,
          },
        }
      );

      router.push('/dashboard');
    } catch (err) {
      alert('Login failed');
    }
  };

  return (
    <main className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl mb-4">Login</h1>
      <input
        type="email"
        placeholder="Email"
        className="input"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        className="input mt-2"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button className="btn mt-4" onClick={handleLogin}>
        Login
      </button>
    </main>
  );
}
