// src/pages/Members.jsx
import { useEffect, useState } from 'react';
import api from 'api/api';
import MemberForm from 'components/memberForm';

export default function Members() {
  const [members, setMembers] = useState([]);
  const [editingMember, setEditingMember] = useState(null);

  const fetchMembers = async () => {
    const res = await api.get('/members');
    setMembers(res.data);
  };

  useEffect(() => {
    fetchMembers();
  }, []);

  const deleteMember = async (id) => {
    await api.delete(`/members/${id}`);
    fetchMembers();
  };

  return (
    <div>
      <h2>Members</h2>

      <MemberForm
        fetchMembers={fetchMembers}
        editingMember={editingMember}
        setEditingMember={setEditingMember}
      />

      <ul>
        {members.map((m) => (
          <li key={m.id}>
            {m.name} - {m.phone}
            <button onClick={() => setEditingMember(m)}>Edit</button>
            <button onClick={() => deleteMember(m.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
