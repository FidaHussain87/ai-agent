
import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface PipelineState {
  pipelines: any[]
}

const initialState: PipelineState = {
  pipelines: [],
}

const pipelineSlice = createSlice({
  name: 'pipelines',
  initialState,
  reducers: {
    setPipelines(state, action: PayloadAction<any[]>) {
      state.pipelines = action.payload
    },
  },
})

export const { setPipelines } = pipelineSlice.actions
export default pipelineSlice.reducer
