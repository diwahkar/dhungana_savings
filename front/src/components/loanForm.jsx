import { useEffect, useState } from 'react';
import api from 'api/api';

export default function LoanForm({
  fetchLoans,
  editingLoan,
  setEditingLoan,
}) {
  const [memberId, setMemberId] = useState('');
  const [amount, setAmount] = useState('');

  useEffect(() => {
    if (editingLoan) {
      setMemberId(editingLoan.memberId);
      setAmount(editingLoan.amount);
    }
  }, [editingLoan]);

  const submit = async (e) => {
    e.preventDefault();

    if (editingLoan) {
      await api.put(`/loans/${editingLoan.id}`, {
        memberId,
        amount,
      });
      setEditingLoan(null);
    } else {
      await api.post('/loans', {
        memberId,
        amount,
      });
    }

    setMemberId('');
    setAmount('');
    fetchLoans();
  };

  return (
    <form onSubmit={submit}>
      <input
        placeholder='Member ID'
        value={memberId}
        onChange={(e) => setMemberId(e.target.value)}
      />
      <input
        placeholder='Loan Amount'
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button type='submit'>
        {editingLoan ? 'Update Loan' : 'Add Loan'}
      </button>
    </form>
  );
}
