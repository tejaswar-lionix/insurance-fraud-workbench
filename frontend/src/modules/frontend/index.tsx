import React, {useState} from 'react';
export const FrontendView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>FRONTEND - Frontend - workbench UI, graph viz, time</h2><p>workbench</p></div>
};
export default FrontendView;
