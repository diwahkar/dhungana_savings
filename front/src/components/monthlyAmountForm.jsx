import { useEffect, useState } from 'react';
import api from 'api/api';

export default function MonthlyAmountForm({
  fetchSavings,
  editingSaving,
  setEditingSaving,
}) {
  const [memberId, setMemberId] = useState('');
  const [amount, setAmount] = useState('');

  useEffect(() => {
    if (editingSaving) {
      setMemberId(editingSaving.memberId);
      setAmount(editingSaving.amount);
    }
  }, [editingSaving]);

  const submit = async (e) => {
    e.preventDefault();

    if (editingSaving) {
      await api.put(`/savings/${editingSaving.id}`, {
        memberId,
        amount,
      });
      setEditingSaving(null);
    } else {
      await api.post('/savings', {
        memberId,
        amount,
      });
    }

    setMemberId('');
    setAmount('');
    fetchSavings();
  };

  return (
    <form onSubmit={submit}>
      <input
        placeholder='Member ID'
        value={memberId}
        onChange={(e) => setMemberId(e.target.value)}
      />
      <input
        placeholder='Amount'
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button type='submit'>
        {editingSaving ? 'Update Saving' : 'Add Saving'}
      </button>
    </form>
  );
}
