import { configureStore } from '@reduxjs/toolkit'
import authReducer from './slices/autSlice'
import agentReducer from './slices/agentSlice'
import pipelineReducer from './slices/pipelineSlice'

export const store = configureStore({
  reducer: {
    auth: authReducer,
    agents: agentReducer,
    pipelines: pipelineReducer,
  },
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
