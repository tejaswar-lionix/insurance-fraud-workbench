import React, {useState} from 'react';
export const IntegrationsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>INTEGRATIONS - Integrations - DMV, police, medical, ISO</h2><p>DMV</p></div>
};
export default IntegrationsView;
