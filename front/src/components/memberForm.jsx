import { useEffect, useState } from 'react';
import api from 'api/api';

export default function MemberForm({
  fetchMembers,
  editingMember,
  setEditingMember,
}) {
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');

  useEffect(() => {
    if (editingMember) {
      setName(editingMember.name);
      setPhone(editingMember.phone);
    }
  }, [editingMember]);

  const submit = async (e) => {
    e.preventDefault();

    if (editingMember) {
      await api.put(`/members/${editingMember.id}`, {
        name,
        phone,
      });
      setEditingMember(null);
    } else {
      await api.post('/members', { name, phone });
    }

    setName('');
    setPhone('');
    fetchMembers();
  };

  return (
    <form onSubmit={submit}>
      <input
        placeholder='Name'
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        placeholder='Phone'
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />
      <button type='submit'>
        {editingMember ? 'Update' : 'Add'}
      </button>
    </form>
  );
}
