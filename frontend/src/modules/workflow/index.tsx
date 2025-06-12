import React, {useState} from 'react';
export const WorkflowView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>WORKFLOW - Workflow - triage, assignment, SLA, esca</h2><p>triage</p></div>
};
export default WorkflowView;
