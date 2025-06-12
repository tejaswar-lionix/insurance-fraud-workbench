import React, {useState} from 'react';
export const ApiView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>API - API - REST for claims, entities, graph</h2><p>POST claim</p></div>
};
export default ApiView;
