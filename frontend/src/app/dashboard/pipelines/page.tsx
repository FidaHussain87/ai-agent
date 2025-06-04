'use client'

import dynamic from 'next/dynamic'

const PipelineBuilder = dynamic(() => import('@/components/PipelineBuilder'), { ssr: false })

export default function PipelinesPage() {
  return (
    <div className="p-4">
      <PipelineBuilder />
    </div>
  )
}
