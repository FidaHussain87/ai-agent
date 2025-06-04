
import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface AgentState {
  agents: any[]
}

const initialState: AgentState = {
  agents: [],
}

const agentSlice = createSlice({
  name: 'agents',
  initialState,
  reducers: {
    setAgents(state, action: PayloadAction<any[]>) {
      state.agents = action.payload
    },
  },
})

export const { setAgents } = agentSlice.actions
export default agentSlice.reducer
